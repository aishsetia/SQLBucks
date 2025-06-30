package com.sqlbucks.SQLBucks.dto;

import lombok.Data;

@Data
public class CustomerDTO {
    private Integer custId;
    private String name;
    private String address;
    private String dob;
    private String gender;
    private String phone;
    private String emailId;
    private String occupation;
} 