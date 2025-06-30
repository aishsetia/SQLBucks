package com.sqlbucks.SQLBucks.controller.dto;

import com.sqlbucks.SQLBucks.domain.Customer;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class RegistrationRequest {
    private Customer customer;
    private String password;
} 