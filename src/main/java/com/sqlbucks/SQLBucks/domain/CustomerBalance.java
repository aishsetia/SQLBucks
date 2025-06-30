package com.sqlbucks.SQLBucks.domain;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.MapsId;
import jakarta.persistence.OneToOne;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDateTime;

@Entity
@Getter
@Setter
@NoArgsConstructor
@Table(name = "customer_balance")
public class CustomerBalance {

    @Id
    @Column(name = "cust_id")
    private Integer custId;

    @OneToOne
    @MapsId
    @JoinColumn(name = "cust_id")
    private Customer customer;

    private Double balance;

    private LocalDateTime lastTransactionTime;
} 