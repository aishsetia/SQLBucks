package com.sqlbucks.SQLBucks.domain;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import jakarta.persistence.OneToOne;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.List;

@Entity
@Getter
@Setter
@NoArgsConstructor
@Table(name = "customer_details")
public class Customer {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "cust_id")
    private Integer custId;

    private String name;

    private String address;

    private String dob;

    private String gender;

    private String phone;

    @Column(name = "email_id", unique = true)
    private String emailId;

    private String occupation;

    @OneToOne(mappedBy = "customer")
    private User user;

    @OneToOne(mappedBy = "customer")
    private CustomerBalance balance;

    @OneToMany(mappedBy = "sender")
    private List<Transaction> sentTransactions;

    @OneToMany(mappedBy = "receiver")
    private List<Transaction> receivedTransactions;
} 