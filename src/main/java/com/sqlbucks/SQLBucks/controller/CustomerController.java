package com.sqlbucks.SQLBucks.controller;

import com.sqlbucks.SQLBucks.controller.dto.RegistrationRequest;
import com.sqlbucks.SQLBucks.domain.Customer;
import com.sqlbucks.SQLBucks.service.CustomerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/customers")
public class CustomerController {

    @Autowired
    private CustomerService customerService;

    @GetMapping("/{id}")
    public ResponseEntity<Customer> getCustomerById(@PathVariable Integer id) {
        return customerService.getCustomerById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping("/register")
    public Customer registerCustomer(@RequestBody RegistrationRequest registrationRequest) {
        return customerService.registerCustomer(registrationRequest.getCustomer(), registrationRequest.getPassword());
    }
} 