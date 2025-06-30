package com.sqlbucks.SQLBucks.repository;

import com.sqlbucks.SQLBucks.domain.CustomerBalance;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CustomerBalanceRepository extends JpaRepository<CustomerBalance, Integer> {
} 