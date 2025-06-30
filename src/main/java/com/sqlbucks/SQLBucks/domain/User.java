package com.sqlbucks.SQLBucks.domain;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.OneToOne;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Getter
@Setter
@NoArgsConstructor
@Table(name = "credentials")
public class User {

    @Id
    @Column(length = 50)
    private String userid;

    @Column(name = "pwd_hash", nullable = false)
    private String pwdHash;

    @OneToOne
    @JoinColumn(name = "cust_id", referencedColumnName = "cust_id")
    private Customer customer;

    private boolean admin;
} 