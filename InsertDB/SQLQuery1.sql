CREATE TABLE [dbo].[Proball_confrontos] (
    [id]             INT           IDENTITY (1, 1) NOT NULL,
    [LIGA]           VARCHAR (500) NULL,
    [DATA_CONFRONTO] DATETIME      NULL,
    [CONFRONTO_CASA]      VARCHAR (500) NULL,
	[CONFRONTO_FORA]      VARCHAR (500) NULL,
    [PLACAR_CASA]           VARCHAR (500) NULL,
    [PLACAR_FORA]           VARCHAR (500) NULL,
    [LINK_EVENTOS]   VARCHAR (500) NULL,
    PRIMARY KEY CLUSTERED ([id] ASC)
);

Truncate table [dbo].[Proball_confrontos]

SELECT * FROM [dbo].[Proball_confrontos]
order by DATA_CONFRONTO


where CONFRONTO_CASA = ('PALMEIRAS')

INSERT INTO [dbo].[Proball_confrontos] (LIGA,DATA_CONFRONTO,CONFRONTO,CASA,FORA,LINK_EVENTOS) VALUES ('','','','','','')

