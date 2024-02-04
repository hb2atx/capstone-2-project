import axios from "axios";

const BASE_URL = process.env.REACT_APP_BASE_URL || "http://localhost:3001";

class OverPaidApi {
  // the token for interactive with the API will be stored here.
  static token;

  static async request(endpoint, data = {}, method = "get") {
    console.debug("API Call:", endpoint, data, method);

    const url = `${BASE_URL}/${endpoint}`;
    const headers = { Authorization: `Bearer ${OverPaidApi.token}` };
    const params = method === "get" ? data : {};

    try {
      return (await axios({ url, method, data, params, headers })).data;
    } catch (err) {
      console.error("API Error:", err.response);
      let message = err.response.data.error.message;
      throw Array.isArray(message) ? message : [message];
    }
  }

  // Individual API routes

  //////////////////////// Get current user /////////////////////////////////////

  static async getCurrentUser(username) {
    let res = await this.request(`user/${username}`);
    return res.user;
  }

  ///////////////////// Signup for the site ////////////////////////////////////

  static async signup(data) {
    let res = await this.request(`auth/register`, data, "post");
    return res.token;
  }

  //////////////// Get token for login from username, password ////////////////////////////////////

  static async login(data) {
    let res = await this.request(`auth/token`, data, "post");
    return res.token;
  }

  //////////////////// Save user profile page //////////////////////////////////

  static async saveProfile(username, data) {
    let res = await this.request(`user/${username}`, data, "patch");
    return res.user;
  }

  ////////////////// Get all NBA player stats //////////////////////////////////

  static async getAllPlayerStats() {
    let res = await this.request(`player/stats`, null, "get");
    return res.player;
  }

    ///////////// Get specific NBA player stats by name //////////////////////////////////

    static async getPlayerStatsByName(playerName) {
      try {
        const res = await this.request(`player/stats/${playerName}`, null, "get");
        return res.player;
      } catch (err) {
        console.error(`Error fetching player stats for ${playerName}:`, err.response);
        throw err;
      }
    }

  ////////////////// Get avg player stats from all positions ///////////////////////////////////

  static async getAllAvgStats() {
    let res = await this.request(`avg`, null, "get");
    return res.avg;
  }

    //////////////////////// Get average stats for a specific position ////////////////////////////////

    static async getAvgStatsByPosition(position) {
      try {
        const res = await this.request(`avg/${position}`, null, "get");
        return res.avg;
      } catch (err) {
        console.error(`Error fetching average stats for ${position}:`, err.response);
        throw err;
      }
    }
  }

export default OverPaidApi;





 








