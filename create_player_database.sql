
-- Table: players
CREATE TABLE players ( 
    id     INT     PRIMARY KEY
                   NOT NULL
                   UNIQUE,
    name   VARCHAR UNIQUE,
    wins   INT,
    losses INT 
);

INSERT INTO [players] ([id], [name], [wins], [losses]) VALUES (0, 'Guest', null, null);
