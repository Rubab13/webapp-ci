package com.example;

import org.junit.*;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.*;

public class AppTest {
    WebDriver driver;

    @Before
    public void setUp() {
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless", "--no-sandbox", "--disable-dev-shm-usage");
        driver = new ChromeDriver(options);

        // Run your local site OR deploy it and change the URL here
        // driver.get("file://" + System.getProperty("user.dir") + "/src/main/webapp/index.html");
        driver.get("http://localhost:8081/index.html");
    }

    @Test
    public void testHeadingExists() {
        WebElement heading = driver.findElement(By.id("heading"));
        Assert.assertEquals("Hello from Web!", heading.getText());
    }

    @After
    public void tearDown() {
        driver.quit();
    }
}
