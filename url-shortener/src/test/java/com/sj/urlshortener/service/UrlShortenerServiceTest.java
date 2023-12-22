package com.sj.urlshortener.service;

import com.sj.urlshortener.model.UrlMapping;
import com.sj.urlshortener.repository.UrlMappingRepository;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import org.springframework.transaction.annotation.Transactional;

import org.junit.jupiter.api.BeforeEach;

import static org.junit.jupiter.api.Assertions.*;


@SpringBootTest
class UrlShortenerServiceTest {


    private UrlShortenerService urlShortenerService;

    @Autowired
    private UrlMappingRepository urlMappingRepository;

    @Autowired
    public UrlShortenerServiceTest(UrlShortenerService urlShortenerService, UrlMappingRepository urlMappingRepository) {
        this.urlShortenerService = urlShortenerService;
        this.urlMappingRepository = urlMappingRepository;
    }

    @Test
    @Transactional
    void testShortenAndRetrieveUrl() {
        // Given
        String originalUrl = "https://www.example.com";

        // When
        String shortUrl = urlShortenerService.shortenUrl(originalUrl);
        UrlMapping urlMapping = urlMappingRepository.findByOriginalUrl(originalUrl);

        // Then
        assertNotNull(shortUrl, "Shortened URL should not be null");
        assertNotNull(urlMapping, "UrlMapping should not be null");
        assertEquals(originalUrl, urlMapping.getOriginalUrl(), "Original URL should match");
    }

    @Test
    void testInvalidShortUrlRedirection() {
        // Given
        String invalidShortUrl = "https://yourdomain.com/invalid";

        // When
        String redirectionUrl = urlShortenerService.getOriginalUrl(invalidShortUrl);

        // Then
        assertNull(redirectionUrl, "Redirection URL should be null");
    }

    // Add more tests based on your application's functionality
}
