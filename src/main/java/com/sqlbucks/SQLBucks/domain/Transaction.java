package com.sqlbucks.SQLBucks.domain;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDateTime;

@Entity
@Getter
@Setter
@NoArgsConstructor
@Table(name = "transactions")
public class Transaction {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "transac_id")
    private Integer transacId;

    @ManyToOne
    @JoinColumn(name = "dcust", referencedColumnName = "cust_id")
    private Customer sender;

    @ManyToOne
    @JoinColumn(name = "ccust", referencedColumnName = "cust_id")
    private Customer receiver;

    private Double amount;

    private LocalDateTime timestamp;
} 