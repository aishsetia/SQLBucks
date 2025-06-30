package com.sqlbucks.SQLBucks.service;

import com.sqlbucks.SQLBucks.domain.Customer;
import com.sqlbucks.SQLBucks.domain.CustomerBalance;
import com.sqlbucks.SQLBucks.domain.User;
import com.sqlbucks.SQLBucks.repository.CustomerRepository;
import com.sqlbucks.SQLBucks.repository.CustomerBalanceRepository;
import com.sqlbucks.SQLBucks.repository.UserRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.server.ResponseStatusException;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

import com.sqlbucks.SQLBucks.dto.CustomerDTO;

@Service
public class CustomerService {

    private static final Logger logger = LoggerFactory.getLogger(CustomerService.class);

    @Autowired
    private CustomerRepository customerRepository;

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private CustomerBalanceRepository customerBalanceRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;

    public Optional<Customer> getCustomerById(Integer id) {
        Optional<Customer> customer = customerRepository.findById(id);
        if (customer.isPresent()) {
            return customer;
        } else {
            logger.error("Customer not found with ID: {}", id);
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Customer not found");
        }
    }

    @Transactional
    public Customer registerCustomer(Customer customer, String password) {
        try {
            logger.info("Starting customer registration for: {}", customer.getName());
            customer.setCustId(null);
            Customer newCustomer = customerRepository.save(customer);
            logger.info("Saved new customer with ID: {}", newCustomer.getCustId());

            // Create and save the user
            User user = new User();
            user.setPwdHash(passwordEncoder.encode(password));
            user.setCustomer(newCustomer);
            user.setAdmin(false);
            userRepository.save(user);
            logger.info("Saved user for customer ID: {}", newCustomer.getCustId());

            // Create and save the customer balance
            CustomerBalance customerBalance = new CustomerBalance();
            customerBalance.setCustomer(newCustomer);
            customerBalance.setBalance(0.0);
            customerBalanceRepository.save(customerBalance);
            logger.info("Saved customer balance for customer ID: {}", newCustomer.getCustId());

            logger.info("Successfully registered customer: {}", newCustomer.getName());
            return newCustomer;
        } catch (Exception e) {
            logger.error("Error during customer registration for: {}", customer.getName(), e);
            throw new RuntimeException("Failed to register customer. Transaction rolled back.", e);
        }
    }

    public CustomerDTO toCustomerDTO(Customer customer) {
        CustomerDTO dto = new CustomerDTO();
        dto.setCustId(customer.getCustId());
        dto.setName(customer.getName());
        dto.setAddress(customer.getAddress());
        dto.setDob(customer.getDob());
        dto.setGender(customer.getGender());
        dto.setPhone(customer.getPhone());
        dto.setEmailId(customer.getEmailId());
        dto.setOccupation(customer.getOccupation());
        return dto;
    }
} 