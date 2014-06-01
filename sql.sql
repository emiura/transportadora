
/* Tabela: Cadastro de Localidades */
CREATE TABLE Localidades (
    locCodigo Serial unique not null,
    locNome Char(25),
    locUF Char(2),
    locDistFil Integer,
    filCodigo BigInt unsigned,
    locISS Numeric(10,2),
   PRIMARY KEY (locCodigo)
) ENGINE = InnoDB;

/* Tabela: Cadastro de Filiais */
CREATE TABLE Filiais (
    filCodigo Serial unique not null,
    filEnder Char(30),
    filBairro Char(20),
    filFone Char(15),
    locCodigo BigInt unsigned,
   PRIMARY KEY (filCodigo)
) ENGINE = InnoDB;

/* Tabela: Tabela de Rotas */
CREATE TABLE Rotas (
    rtaCodigo Serial unique not null,
    rtaNome Char(15),
    rtaQtInterm Integer,
    filCodigo BigInt unsigned not null,
   PRIMARY KEY (rtaCodigo)
) ENGINE = InnoDB;

/* Tabela: Filiais intermediárias de rotas */
CREATE TABLE RotasInterm (
    rtaCodigo BigInt unsigned not null,
    rtiSeq Integer not null,
    rtiKm Char(10),
    filCodigo BigInt unsigned not null,
   PRIMARY KEY (rtaCodigo,rtiSeq)
) ENGINE = InnoDB;

/* Tabela: Cadastro de Funcionários */
CREATE TABLE Funcionarios (
    funCodigo Serial unique not null,
    funNome Char(30),
    funEnder Char(30),
    funFone Char(15),
    funDtNasc Date,
    funClasse Char(1),
    funCateg Char(4),
   PRIMARY KEY (funCodigo)
) ENGINE = InnoDB;

/* Tabela: Cadastro de Veículos */
CREATE TABLE Veiculos (
    veiCodigo Serial unique not null,
    veiDescr Char(20),
    veiAno Integer,
    veiPlaca Char(8),
    veiKm Integer,
    veiCateg Char(5),
   PRIMARY KEY (veiCodigo)
) ENGINE = InnoDB;

/* Tabela: Cadastro de Clientes */
CREATE TABLE Clientes (
    CodCliente Serial unique not null,
    Nome Char(30),
    Endereco Char(30),
    Fone Char(15),
    locCodigo BigInt unsigned not null,
   PRIMARY KEY (CodCliente)
) ENGINE = InnoDB;

/* Tabela: Registro de Ordens de Despacho */
CREATE TABLE Ordens (
    ordNumero Integer not null,
    ordData Date,
    ordQtItens Integer,
    ordVltotal Decimal(10,2),
    CodOrigem BigInt unsigned,
    CodDestino BigInt unsigned,
    CodRemetente BigInt unsigned,
    CodDestinatario BigInt unsigned,
    funCodigo BigInt unsigned not null,
    ordICMS Numeric(10,2),
    ordISS Numeric(10,2),
    ordTipo Char(1),
   PRIMARY KEY (ordNumero)
) ENGINE = InnoDB;

/* Tabela: Itens de Ordens de Despacho */
CREATE TABLE Volumes (
    ordNumero Integer not null,
    volSeq Integer not null,
    volDescr Char(30),
    volPeso Decimal(10,3),
    volValor Decimal(10,2),
    volVlFrete Decimal(10,2),
    volVolume Decimal(10,2),
    volCubagem Decimal(10,2),
   PRIMARY KEY (ordNumero,volSeq)
) ENGINE = InnoDB;

/* Tabela: Controles de Cargas */
CREATE TABLE Cargas (
    viaNumero Integer not null,
    cgaNumero Integer not null,
    filCodigo BigInt unsigned not null,
    funCodigo BigInt unsigned not null,
   PRIMARY KEY (viaNumero,cgaNumero)
) ENGINE = InnoDB;

/* Tabela: Itens de Controles de Cargas */
CREATE TABLE CargasItens (
    cgaNumero Integer not null,
    viaNumero Integer not null,
    SeqCarga Char(10) not null,
    ordNumero Integer not null,
   PRIMARY KEY (cgaNumero,viaNumero,SeqCarga)
) ENGINE = InnoDB;

/* Tabela: Ordens de Descargas */
CREATE TABLE Descargas (
    viaNumero Integer not null,
    dscNumero Integer not null,
    filCodigo BigInt unsigned not null,
    dscData Date,
    funCodigo BigInt unsigned not null,
   PRIMARY KEY (viaNumero,dscNumero)
) ENGINE = InnoDB;

/* Tabela: Itens de Controles de Descargas */
CREATE TABLE DescargasItens (
    viaNumero Integer not null,
    dscNumero Integer not null,
    SeqDescg Char(10) not null,
    ordNumero Integer not null,
   PRIMARY KEY (viaNumero,dscNumero,SeqDescg)
) ENGINE = InnoDB;

/* Tabela: Registro de Viagens */
CREATE TABLE Viagens (
    viaNumero Integer not null,
    viaData Date,
    viaObs Char(80),
    viaKmIni Integer,
    viaKmFim Integer,
    veiCodigo BigInt unsigned not null,
    funCodigo BigInt unsigned not null,
    rtaCodigo BigInt unsigned not null,
   PRIMARY KEY (viaNumero)
) ENGINE = InnoDB;

/* Tabela: Distâncias entre filiais */
CREATE TABLE FiliaisDist (
    CodOrigem BigInt unsigned not null,
    CodDestino BigInt unsigned not null,
    Distancia Integer,
   PRIMARY KEY (CodOrigem,CodDestino)
) ENGINE = InnoDB;

/* Tabela: Tabela de Preços */
CREATE TABLE Precos (
    prcDtVig Date not null,
    prcVlFixo Decimal(10,2),
    prcKmKg Decimal(10,2),
    prcKmEsp Decimal(10,2),
   PRIMARY KEY (prcDtVig)
) ENGINE = InnoDB;

/* Tabela: (null) */
CREATE TABLE Vencimentos (
    veiCodigo BigInt unsigned not null,
    venSeq Integer not null,
    venDescr Char(20),
    venValor Decimal(10,2),
    venDtVenc Date,
    venDtQuit Date,
   PRIMARY KEY (veiCodigo,venSeq)
) ENGINE = InnoDB;

/* Tabela: (null) */
CREATE TABLE Despesas (
    veiCodigo BigInt unsigned not null,
    dspSeq Integer not null,
    dspData Date,
    dspDescr Char(20),
    dspValor Decimal(10,2),
    dspKmVei Integer,
   PRIMARY KEY (veiCodigo,dspSeq)
) ENGINE = InnoDB;

/* Tabela: tabela de rodovias */
CREATE TABLE Rodovias (
    rodCodigo Char(10) not null,
    rodNome Char(10),
   PRIMARY KEY (rodCodigo)
) ENGINE = InnoDB;

/* Tabela: Rotas e rodovias */
CREATE TABLE RotasRodovias (
    rodCodigo Char(10) not null,
    rtaCodigo BigInt unsigned not null,
    rrvSeq Integer not null,
    rrvKmIni Integer,
    rrvKmFim Integer,
    rrvQtPed Integer,
    rrvVlPed Numeric(10,2),
   PRIMARY KEY (rodCodigo,rtaCodigo,rrvSeq)
) ENGINE = InnoDB;

/* Relacionamentos */
ALTER TABLE Filiais ADD CONSTRAINT FK_Filiais_16 FOREIGN KEY (locCodigo) REFERENCES Localidades(locCodigo);
ALTER TABLE Localidades ADD CONSTRAINT FK_Localidades_17 FOREIGN KEY (filCodigo) REFERENCES Filiais(filCodigo);
ALTER TABLE Rotas ADD CONSTRAINT FK_Rotas_18 FOREIGN KEY (filCodigo) REFERENCES Filiais(filCodigo);
ALTER TABLE RotasInterm ADD CONSTRAINT FK_RotasInterm_19 FOREIGN KEY (rtaCodigo) REFERENCES Rotas(rtaCodigo);
ALTER TABLE Ordens ADD CONSTRAINT FK_Ordens_20 FOREIGN KEY (funCodigo) REFERENCES Funcionarios(funCodigo);
ALTER TABLE Ordens ADD CONSTRAINT FK_Ordens_21 FOREIGN KEY (CodRemetente) REFERENCES Clientes(CodCliente);
ALTER TABLE Viagens ADD CONSTRAINT FK_Viagens_22 FOREIGN KEY (veiCodigo) REFERENCES Veiculos(veiCodigo);
ALTER TABLE Volumes ADD CONSTRAINT FK_Volumes_23 FOREIGN KEY (ordNumero) REFERENCES Ordens(ordNumero);
ALTER TABLE Viagens ADD CONSTRAINT FK_Viagens_24 FOREIGN KEY (funCodigo) REFERENCES Funcionarios(funCodigo);
ALTER TABLE Cargas ADD CONSTRAINT FK_Cargas_25 FOREIGN KEY (viaNumero) REFERENCES Viagens(viaNumero);
ALTER TABLE Descargas ADD CONSTRAINT FK_Descargas_27 FOREIGN KEY (viaNumero) REFERENCES Viagens(viaNumero);
ALTER TABLE CargasItens ADD CONSTRAINT FK_CargasItens_28 FOREIGN KEY (viaNumero,cgaNumero) REFERENCES Cargas(viaNumero,cgaNumero);
ALTER TABLE DescargasItens ADD CONSTRAINT FK_DescargasItens_29 FOREIGN KEY (viaNumero,dscNumero) REFERENCES Descargas(viaNumero,dscNumero);
ALTER TABLE Ordens ADD CONSTRAINT FK_Ordens_34 FOREIGN KEY (CodOrigem) REFERENCES Filiais(filCodigo);
ALTER TABLE RotasInterm ADD CONSTRAINT FK_RotasInterm_36 FOREIGN KEY (filCodigo) REFERENCES Filiais(filCodigo);
ALTER TABLE Viagens ADD CONSTRAINT FK_Viagens_37 FOREIGN KEY (rtaCodigo) REFERENCES Rotas(rtaCodigo);
ALTER TABLE Cargas ADD CONSTRAINT FK_Cargas_38 FOREIGN KEY (filCodigo) REFERENCES Filiais(filCodigo);
ALTER TABLE Descargas ADD CONSTRAINT FK_Descargas_39 FOREIGN KEY (filCodigo) REFERENCES Filiais(filCodigo);
ALTER TABLE Clientes ADD CONSTRAINT FK_Clientes_40 FOREIGN KEY (locCodigo) REFERENCES Localidades(locCodigo);
ALTER TABLE Ordens ADD CONSTRAINT FK_Ordens_41 FOREIGN KEY (CodDestinatario) REFERENCES Clientes(CodCliente);
ALTER TABLE CargasItens ADD CONSTRAINT FK_CargasItens_42 FOREIGN KEY (ordNumero) REFERENCES Ordens(ordNumero);
ALTER TABLE DescargasItens ADD CONSTRAINT FK_DescargasItens_43 FOREIGN KEY (ordNumero) REFERENCES Ordens(ordNumero);
ALTER TABLE FiliaisDist ADD CONSTRAINT FK_FiliaisDist_45 FOREIGN KEY (CodDestino) REFERENCES Filiais(filCodigo);
ALTER TABLE FiliaisDist ADD CONSTRAINT FK_FiliaisDist_46 FOREIGN KEY (CodOrigem) REFERENCES Filiais(filCodigo);
ALTER TABLE Ordens ADD CONSTRAINT FK_Ordens_49 FOREIGN KEY (CodDestino) REFERENCES Localidades(locCodigo);
ALTER TABLE Vencimentos ADD CONSTRAINT FK_Vencimentos_51 FOREIGN KEY (veiCodigo) REFERENCES Veiculos(veiCodigo);
ALTER TABLE Despesas ADD CONSTRAINT FK_Despesas_53 FOREIGN KEY (veiCodigo) REFERENCES Veiculos(veiCodigo);
ALTER TABLE RotasRodovias ADD CONSTRAINT FK_RotasRodovias_56 FOREIGN KEY (rtaCodigo) REFERENCES Rotas(rtaCodigo);
ALTER TABLE RotasRodovias ADD CONSTRAINT FK_RotasRodovias_57 FOREIGN KEY (rodCodigo) REFERENCES Rodovias(rodCodigo);
ALTER TABLE Descargas ADD CONSTRAINT FK_Descargas_58 FOREIGN KEY (funCodigo) REFERENCES Funcionarios(funCodigo);
ALTER TABLE Cargas ADD CONSTRAINT FK_Cargas_59 FOREIGN KEY (funCodigo) REFERENCES Funcionarios(funCodigo);

/* Indices */
CREATE UNIQUE INDEX Localidades_PK ON Localidades (locCodigo);
CREATE UNIQUE INDEX Filiais_PK ON Filiais (filCodigo);
CREATE UNIQUE INDEX Rotas_PK ON Rotas (rtaCodigo);
CREATE UNIQUE INDEX RotasInterm_PK ON RotasInterm (rtaCodigo,rtiSeq);
CREATE UNIQUE INDEX Funcionarios_PK ON Funcionarios (funCodigo);
CREATE UNIQUE INDEX Veiculos_PK ON Veiculos (veiCodigo);
CREATE UNIQUE INDEX Clientes_PK ON Clientes (CodCliente);
CREATE UNIQUE INDEX Ordens_PK ON Ordens (ordNumero);
CREATE UNIQUE INDEX Volumes_PK ON Volumes (ordNumero,volSeq);
CREATE UNIQUE INDEX Cargas_PK ON Cargas (viaNumero,cgaNumero);
CREATE UNIQUE INDEX CargasItens_PK ON CargasItens (cgaNumero,viaNumero,SeqCarga);
CREATE UNIQUE INDEX Descargas_PK ON Descargas (viaNumero,dscNumero);
CREATE UNIQUE INDEX DescargasItens_PK ON DescargasItens (viaNumero,dscNumero,SeqDescg);
CREATE UNIQUE INDEX Viagens_PK ON Viagens (viaNumero);
CREATE UNIQUE INDEX FiliaisDist_PK ON FiliaisDist (CodOrigem,CodDestino);
CREATE UNIQUE INDEX Precos_PK ON Precos (prcDtVig);
CREATE UNIQUE INDEX Vencimentos_PK ON Vencimentos (veiCodigo,venSeq);
CREATE UNIQUE INDEX Despesas_PK ON Despesas (veiCodigo,dspSeq);
CREATE UNIQUE INDEX Rodovias_PK ON Rodovias (rodCodigo);
CREATE UNIQUE INDEX RotasRodovias_PK ON RotasRodovias (rodCodigo,rtaCodigo,rrvSeq);

/* Triggers */
