package com.sqlbucks.SQLBucks.repository;

import com.sqlbucks.SQLBucks.domain.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository extends JpaRepository<User, String> {
} 