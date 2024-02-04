const jsonschema = require("jsonschema");
const express = require("express");
const db = require("../db");
const router = express.Router();

//////////// Return stats for all NBA players ///////////////////

router.get("/stats", async function (req, res, next) {
    try {
        const results = await db.query(`SELECT * FROM players_stats`)
        return res.json(results.rows)
    }
    catch (err) {
        return next(err)
    }
});

///////////////// Returns stats for a specific NBA player //////////////////////

router.get("/stats/:name", async function (req, res, next) {
    const playerName = decodeURIComponent(req.params.name.replace(/\+/g, ' '));

    try {
        const playerStats = await db.query(
            `SELECT * FROM players_stats WHERE players_name = $1`,
            [playerName]
        );

        if (playerStats.rows.length === 0) {
            return res.status(404).json({ message: `No stats found for the specified player: ${playerName}` });
        }

        const playerStatistics = playerStats.rows[0];

        return res.json({ player: playerStatistics });
    } catch (err) {
        return next(err);
    }
});

//////////////// Get NBA player stats by position //////////////////////////////

// router.get("/stats/:position", async function (req, res, next) {
//     const position = req.params.position.toUpperCase();

//     try {
//         const playersStats = await db.query(
//             `SELECT * FROM players_stats WHERE position = $1`,
//             [position]
//         );

//         if (playersStats.rows.length === 0) {
//             return res.status(404).json({ message: `No players found for the specified position: ${position}` });
//         }

//         const playersStatistics = playersStats.rows;

//         return res.json({ players: playersStatistics });
//     } catch (err) {
//         return next(err);
//     }
// });

module.exports = router;