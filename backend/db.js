
const { Client } = require("pg");
const { getDatabaseUri } = require("./config");

let DB_URI;

if(process.env.NODE_ENV === "test") {
  DB_URI = "postgresql:///overpaid_test";
} else {
  DB_URI = "postgresql:///overpaid";
}
let db = new Client({
  host: "/var/run/postgresql",
  database: "overpaid",
});

db.connect();

module.exports = db;