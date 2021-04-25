import axios from "axios";

//******************************CONSTANTS******************************
const initialData = {
  array: [],
};

//******************************TYPES******************************
const GET_GAMES_INFO = "GET_GAMES_INFO";

//******************************REDUCER******************************
export default function gamesReducer(state = initialData, action) {
  switch (action.type) {
    case GET_GAMES_INFO:
      return {
        ...state,
        array: action.payload.array,
      };

    default:
      return state;
  }
}

//******************************ACTIONS******************************
//Action to get games's list
export const getGamesInfoActions = () => async (dispatch, getState) => {
  try {
    await axios.get(`${process.env.REACT_APP_API_URL}getGames`)
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
