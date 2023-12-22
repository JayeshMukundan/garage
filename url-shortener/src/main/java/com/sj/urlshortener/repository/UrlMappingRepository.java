package com.sj.urlshortener.repository;

import com.sj.urlshortener.model.UrlMapping;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UrlMappingRepository extends JpaRepository<UrlMapping, Long> {

    UrlMapping findByShortId(String shortId);

    UrlMapping findByOriginalUrl(String originalUrl);

}
