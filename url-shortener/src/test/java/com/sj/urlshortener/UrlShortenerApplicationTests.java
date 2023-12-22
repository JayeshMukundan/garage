package com.sj.urlshortener;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.context.ApplicationContext;

import static org.junit.jupiter.api.Assertions.assertNotNull;

@SpringBootTest
class UrlShortenerApplicationTests {

	public UrlShortenerApplicationTests(ApplicationContext applicationContext) {
		this.applicationContext = applicationContext;
	}

	private ApplicationContext applicationContext;


	@Test
	void contextLoads() {
		assertNotNull(applicationContext, "Application context should not be null");
	}

}
