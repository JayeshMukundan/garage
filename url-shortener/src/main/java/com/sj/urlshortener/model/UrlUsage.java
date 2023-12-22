package com.sj.urlshortener.model;

import java.io.Serializable;
import java.time.Instant;

public class UrlUsage implements Serializable {
    private String shortId;

    private Instant accessedAt;

    private String ipAddress;

    private String userAgent;

    private String country;

    private String timezoneId;

    public String getShortId() {
        return shortId;
    }

    public void setShortId(String shortId) {
        this.shortId = shortId;
    }

    public Instant getAccessedAt() {
        return accessedAt;
    }

    public void setAccessedAt(Instant accessedAt) {
        this.accessedAt = accessedAt;
    }

    public String getIpAddress() {
        return ipAddress;
    }

    public void setIpAddress(String ipAddress) {
        this.ipAddress = ipAddress;
    }

    public String getUserAgent() {
        return userAgent;
    }

    public void setUserAgent(String userAgent) {
        this.userAgent = userAgent;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public String getTimezoneId() {
        return timezoneId;
    }

    public void setTimezoneId(String timezoneId) {
        this.timezoneId = timezoneId;
    }

    @Override
    public String toString() {
        return "UrlUsage{" +
                "shortId='" + shortId + '\'' +
                ", accessedAt=" + accessedAt +
                ", ipAddress='" + ipAddress + '\'' +
                ", userAgent='" + userAgent + '\'' +
                ", country='" + country + '\'' +
                ", timezoneId='" + timezoneId + '\'' +
                '}';
    }
}
