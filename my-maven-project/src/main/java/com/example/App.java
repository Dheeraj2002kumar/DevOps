package com.example;

import java.io.InputStream;
import java.util.Properties;

public class App {
    public static void main(String[] args) {
        System.out.println("Hello, Maven Project!");

        try (InputStream input = App.class.getClassLoader().getResourceAsStream("config.properties")) {
            Properties prop = new Properties();

            if (input == null) {
                System.out.println("Unable to find config.properties");
                return;
            }

            prop.load(input);
            System.out.println("App name: " + prop.getProperty("app.name"));

        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}
