package com.sqlbucks.SQLBucks.repository;

import com.sqlbucks.SQLBucks.domain.Customer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CustomerRepository extends JpaRepository<Customer, Integer> {
} 