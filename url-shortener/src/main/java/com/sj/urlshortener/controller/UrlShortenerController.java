package com.sj.urlshortener.controller;

import com.sj.urlshortener.model.UrlUsage;
import com.sj.urlshortener.pubsub.UrlUsagePublisher;
import com.sj.urlshortener.service.UrlShortenerService;
import jakarta.servlet.http.HttpServletRequest;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.support.RequestContextUtils;

import java.time.Instant;
import java.util.Locale;
import java.util.Optional;
import java.util.TimeZone;

@RestController
@RequestMapping("/api/url")
public class UrlShortenerController {

    private UrlShortenerService urlShortenerService;
    private static final Logger log = LoggerFactory.getLogger(UrlShortenerController.class);

    private UrlUsagePublisher urlUsagePublisher;

    public UrlShortenerController(UrlShortenerService urlShortenerService, UrlUsagePublisher urlUsagePublisher) {
        this.urlShortenerService = urlShortenerService;
        this.urlUsagePublisher = urlUsagePublisher;
    }

    @PostMapping("/shorten")
    public String shortenUrl(@RequestBody String originalUrl) {
        log.info("Original url = {}", originalUrl);
        return urlShortenerService.shortenUrl(originalUrl);
    }

    @GetMapping("redirect/{shortId}")
    public String redirectToOriginalUrl(@PathVariable String shortId, HttpServletRequest request) {
        // Implement logic to retrieve the original URL based on the shortId
        // For example, you can use your service method or repository to fetch the URL
        log.info("Short id = {}", shortId);
        publishUsageInformation(shortId, request);
        return urlShortenerService.getOriginalUrl(shortId);
    }

    /**
     * Publish the usage information for data analytics
     * @param shortId
     * @param request
     */
    private void publishUsageInformation(String shortId, HttpServletRequest request) {
        String ipAddress = request.getRemoteAddr();
        String userAgent = request.getHeader("User-Agent");
        Locale locale = RequestContextUtils.getLocale(request);
        TimeZone timeZone = Optional.ofNullable(RequestContextUtils.getTimeZone(request)).orElse(TimeZone.getDefault());
        String timeZoneId = timeZone.getID();
        UrlUsage urlUsage = new UrlUsage();
        urlUsage.setAccessedAt(Instant.now());
        urlUsage.setCountry(locale.getCountry());
        urlUsage.setIpAddress(ipAddress);
        urlUsage.setShortId(shortId);
        urlUsage.setUserAgent(userAgent);
        urlUsage.setTimezoneId(timeZoneId);

        urlUsagePublisher.publishMessage(urlUsage);
    }


    @PostMapping("/original")
    public String originalUrl(@RequestBody String shortId) {
        log.info("Short id = {}", shortId);
        return urlShortenerService.getOriginalUrl(shortId);
    }

    // You can add more endpoints as needed

}

