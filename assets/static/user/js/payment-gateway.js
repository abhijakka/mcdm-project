function validation(){
    let feedback_name = document.myform.first_name
    let feedback_cause = document.myform.feedback_cause
    let email = document.myform.Email_1
    var mailformat = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    let phoneNum = document.myform.tel

    
    if (phoneNum.value.length != 10) {

        alert("please Enter valid mobile number");
        
        return false;
        
    }

    if (phoneNum.value.length <= 0) {

        alert("Please Enter Mobile Number");

        return false;
    }
 

    if(feedback_name.value.length <= 0){

        alert("Please Enter Your Name:");
        feedback_name.focus();
        return false;
    } 

    if(feedbacks.value.length <= 0){

        alert("Please Write Your Message:");
        feedbacks.focus();
        return false;
    } 


    if(feedback_cause.value.length <= 0){

        alert("Please Write Your Cause:");
        feedback_cause.focus();
        return false;
    } 
    if (!email.value.match(mailformat)){
        alert("invalid email")
        email.focus();
        return false;
       } 
  

}