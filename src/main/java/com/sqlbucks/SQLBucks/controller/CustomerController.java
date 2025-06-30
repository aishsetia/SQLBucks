package com.sqlbucks.SQLBucks.controller;

import com.sqlbucks.SQLBucks.controller.dto.RegistrationRequest;
import com.sqlbucks.SQLBucks.domain.Customer;
import com.sqlbucks.SQLBucks.service.CustomerService;
import com.sqlbucks.SQLBucks.dto.CustomerDTO;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
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

    private static final Logger logger = LoggerFactory.getLogger(CustomerController.class);

    @Autowired
    private CustomerService customerService;

    @GetMapping("/{id}")
    public ResponseEntity<CustomerDTO> getCustomerById(@PathVariable Integer id) {
        return customerService.getCustomerById(id)
                .map(customer -> ResponseEntity.ok(customerService.toCustomerDTO(customer)))
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping("/register")
    public CustomerDTO registerCustomer(@RequestBody RegistrationRequest registrationRequest) {
        logger.info("Received registration request for customer: {}", registrationRequest.getCustomer().getName());
        Customer customer = customerService.registerCustomer(registrationRequest.getCustomer(), registrationRequest.getPassword());
        return customerService.toCustomerDTO(customer);
    }
} 