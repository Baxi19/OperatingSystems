import React from 'react';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import NotificationsIcon from '@material-ui/icons/Notifications';
import TextField from '@material-ui/core/TextField';
import { useDispatch } from "react-redux";
import { notifyActions } from "../../redux/gamesDuck";


const NotificationAlert = React.forwardRef((props, ref) => {
    const dispatch = useDispatch();
    const [open, setOpen] = React.useState(false);
    const [email, setEmail] = React.useState("");

    const handleClickOpen = () => {
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
        setEmail("");
    };
    
    const handleAcept = () => {
        dispatch(notifyActions([email, props.item]));
        setOpen(false);
        setEmail("");
    };

    const handleChange = (e) => {
        setEmail(e.target.value);
    }

    return (
        <>
            <NotificationsIcon fontSize="small" onClick={handleClickOpen} color="primary"/>
            <Dialog
                open={open}
                onClose={handleClose}
                aria-labelledby="alert-dialog-title"
                aria-describedby="alert-dialog-description"
            >
                <DialogTitle id="alert-dialog-title">{"Notify game discounts?"}</DialogTitle>
                <DialogContent>
                <DialogContentText id="alert-dialog-description">
                    <TextField id="standard-basic" label="Email" onChange={handleChange}/>
                </DialogContentText>
                </DialogContent>
                <DialogActions>
                <Button onClick={handleClose} color="primary">
                    Cancel
                </Button>
                <Button onClick={handleAcept} color="primary" autoFocus>
                    Acept
                </Button>
                </DialogActions>
            </Dialog>
        </>
  );
})

export default NotificationAlert;
