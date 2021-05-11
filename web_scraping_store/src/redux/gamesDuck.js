import axios from "axios";

//******************************CONSTANTS******************************
const initialData = {
  array: [],
  subscribers: [],
};

//******************************TYPES******************************
const GET_GAMES_INFO = "GET_GAMES_INFO";
const NOTIFY_EMAIL = "NOTIFY_EMAIL";

//******************************REDUCER******************************
export default function gamesReducer(state = initialData, action) {
  switch (action.type) {
    case GET_GAMES_INFO:
      return {
        ...state,
        array: action.payload.array,
      };

    case NOTIFY_EMAIL:
      return {
        ...state,
        subscribers: action.payload.subscribers,
      };

    default:
      return state;
  }
}

//******************************ACTIONS******************************
//Action to get games's list
export const getGamesInfoActions = () => async (dispatch, getState) => {
  try {
    await axios
      //.get(`${process.env.REACT_APP_API_URL}getGames`)
      .get(`http://127.0.0.1:5000/getGames`)
      .then(async (res) => {
        console.log(res.data.array.length);
        dispatch({
          type: GET_GAMES_INFO,
          payload: {
            array: res.data.array,
          },
        });
      });
  } catch (error) {
    console.log(error);
  }
};

//Action to get games's list
export const notifyActions = (data) => async (dispatch, getState) => {
  try {
    const { subscribers } = getState().games;
    await axios.post(`http://127.0.0.1:5000/email`, data)
      .then(async (res) => {
      dispatch({
        type: NOTIFY_EMAIL,
        payload: {
          subscribers: subscribers.push(data),
        },
      });
    });
  } catch (error) {
    console.log(error);
  }
};
