package com.sj.urlshortener.service;

import com.sj.urlshortener.model.UrlMapping;
import com.sj.urlshortener.repository.UrlMappingRepository;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.security.SecureRandom;

@Service
public class UrlShortenerService {

    private static final Logger log = LoggerFactory.getLogger(UrlShortenerService.class);


    private UrlMappingRepository urlMappingRepository;

    private RedisTemplate<String, String> redisTemplate;

    public UrlShortenerService(UrlMappingRepository urlMappingRepository, RedisTemplate<String, String> redisTemplate) {
        this.urlMappingRepository = urlMappingRepository;
        this.redisTemplate = redisTemplate;
    }

    public String shortenUrl(String originalUrl) {
        // Check if the URL is already shortened
        UrlMapping existingMapping = urlMappingRepository.findByOriginalUrl(originalUrl);
        if (existingMapping != null) {
            return existingMapping.getShortId();
        }

        // Generate a unique short ID (you can use your logic here)
        String shortId = generateShortId();

        // Save the mapping in the database
        UrlMapping urlMapping = new UrlMapping();
        urlMapping.setOriginalUrl(originalUrl);
        urlMapping.setShortId(shortId);
        urlMappingRepository.save(urlMapping);

        // Store the mapping in Redis for caching
        redisTemplate.opsForValue().set(shortId, originalUrl);

        return shortId;
    }

    public String getOriginalUrl(String shortId) {
        // Check Redis cache first
        String originalUrl = redisTemplate.opsForValue().get(shortId);
        log.info("Short id = {}, original url = {}", shortId, originalUrl);

        if (originalUrl == null) {
            // If not in cache, fetch from the database
            UrlMapping urlMapping = urlMappingRepository.findByShortId(shortId);

            if (urlMapping != null) {
                originalUrl = urlMapping.getOriginalUrl();
                // Store in Redis cache for future requests
                redisTemplate.opsForValue().set(shortId, originalUrl);
            }
        }

        return originalUrl;
    }

    /**
     * Generates a short URL with 8 characters.
     *
     * @return Shortened URL
     */
    private String generateShortId() {
        // Define character set for the short URL (alphanumeric characters)
        String characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

        // Length of the shortened URL
        int length = 8;

        // Generate a random short ID
        String shortId = generateRandomString(characters, length);

        return shortId;
    }

    /**
     * Generates a random string of the specified length from the given character set.
     *
     * @param characters Character set
     * @param length     Length of the generated string
     * @return Random string
     */
    private String generateRandomString(String characters, int length) {
        SecureRandom random = new SecureRandom();
        StringBuilder stringBuilder = new StringBuilder(length);

        for (int i = 0; i < length; i++) {
            int randomIndex = random.nextInt(characters.length());
            char randomChar = characters.charAt(randomIndex);
            stringBuilder.append(randomChar);
        }

        return stringBuilder.toString();
    }
}
