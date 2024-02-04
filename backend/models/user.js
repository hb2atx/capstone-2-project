"use strict";
const db = require("../db");
const bcrypt = require("bcrypt");
const {
    NotFoundError,
    BadRequestError,
    UnauthorizedError
} = require("../expressError");
const { BCRYPT_WORK_FACTOR } = require("../config.js");

class User {
    static async authenticate(username, password) {
        const result = await db.query(
            `SELECT username,
            password,
            first_name AS "firstName",
            last_name AS "lastName",
            email,
            is_admin AS "isAdmin"
            FROM users
            WHERE username = $1`,
            [username],
        );
        const user = result.rows[0];

        if(user) {
            const isValid = await bcrypt.compare(password, user.password);
            if(isValid === true) {
                delete user.password;
                return user;
            }
        }

        throw new UnauthorizedError("Invalid username/password")
    }
    static async register({username, password, firstName, lastName, email, isAdmin}) {
        const duplicateCheck = await db.query(
            `SELECT username
            FROM users
            WHERE username = $1`,
            [username],
        );
        if (duplicateCheck .rows[0]) {
            throw new BadRequestError(`Duplicate username: ${username}`);
        }
        const hashedPassword = await bcrypt.hash(password, BCRYPT_WORK_FACTOR);

        const result = await db.query(
            `INSERT INTO users
            (username,
                password,
                first_name,
                last_name,
                email,
                is_admin)
                VALUES ($1, $2, $3, $4, $5, $6)
                RETURNING username, first_name as "firstName", last_name AS "lastName", email, is_admin AS "isAdmin"`,
                [
                    username,hashedPassword,
                    firstName,
                    lastName,
                    email,
                    isAdmin,
                ],
        );

        const user = result.rows[0];

        return user;
    }
    static async findAll() {
        const result = await db.query(
            `SELECT username,
            first_name AS "firstName",
            last_name AS "lastname",
            email,
            is_admin AS "isAdmin"
            FROM users
            ORDER BY username`,
        );

        return result.rows;
    }
    static async get(username, data) {
      if (data.password) {
        data.password = await bcrypt.hash(data.password, BCRYPT_WORK_FACTOR);
      }

      const { setCols, values } = sqlPartialUpdate(
        data,
        {
            firstName: "first_name",
            lastName: "last_name",
            isAdmin: "isAdmin",
        });
        const usernameVarIdx = "$" + (values.length + 1);

        const querySq1 = `UPDATE users
        SET ${setCols}
        WHERE username = ${usernameVarIdx}
        RETURNING username,
        first_name AS "firstName",
        last_name AS "lastName",
        email,
        is_admin AS "isAdmin"`;

        const result = await db.query(querySql, [...values, username]);
        const user = result.rows[0];

        if (!user) throw new NotFoundError(`No user: %{username}`);

        delete user.password;
        return user;
    }
    static async remove(username) {
        let result = await db.query(
            `DELETE
            FROM users
            WHERE username = $1
            RETURNING username`,
            [username],     
        );
        const user = result.rows[0];

        if (!user) throw new NotFoundError(`No user: ${username}`);
    }
    static async remove(username) {
        let result = await db.query(
              `DELETE
               FROM users
               WHERE username = $1
               RETURNING username`,
            [username],
        );
        const user = result.rows[0];
    
        if (!user) throw new NotFoundError(`No user: ${username}`);
      }
}
module.exports = User;

// curl -v -X POST "http://localhost:3001/auth/register" -d '{"username": "someUser", "password": "somePassword", "firstName": "john", "lastName": "doe", "email": "email1@mail.com"}' -H 'content-type: application/json'







