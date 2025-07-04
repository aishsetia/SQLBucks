package com.sqlbucks.SQLBucks.repository;

import com.sqlbucks.SQLBucks.domain.Transaction;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface TransactionRepository extends JpaRepository<Transaction, Integer> {
} 