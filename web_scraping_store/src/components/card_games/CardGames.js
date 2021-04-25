import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import Rating from "@material-ui/lab/Rating";
import Typography from "@material-ui/core/Typography";

const useStyles = makeStyles({
  root: {
    maxWidth: 345,
    margin: "20px",
    width: "350px",
  },
  media: {
    height: 140,
  },
});

const CardGames = React.forwardRef((props, ref) => {
  const classes = useStyles();
  
  return (
    <>
      <Card className={classes.root}>
        <CardActionArea>
          <CardMedia
            className={classes.media}
            image={`${props.item["url"]}?h=400`}
            title="Contemplative Reptile"
          />
          <CardContent>
            <Rating name="read-only" value={5} readOnly /> {/*TODO: Set metadata in value*/}
            <Typography gutterBottom variant="h5" component="h2">
              {`${props.item["name"]}`}
            </Typography>
            <Typography variant="body2" color="textSecondary" component="p">
              Store: {`${props.item["store"]}`}
              <br />
              Price: {`${props.item["price"]}`}
              <br />
              Time: {`${props.item["time"]}`}
            </Typography>
          </CardContent>
        </CardActionArea>
      </Card>
    </>
  );
});

export default CardGames;
