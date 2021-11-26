function addVote(id){
  $.ajax ({
    url: '/update-vote-count',
    type: "GET",
    data: {
      employee_id : id,
    },
    success: function(data) {
      document.getElementById(`vote-button-${id}`).innerHTML = "Vote cast!";
      document.getElementById(`vote-button-${id}`).disabled = true;
      document.getElementById(`vote-count-${id}`).innerHTML = `${data["vote_count"]}`;
      if (data["vote_count"] == 1) {
        document.getElementById("vote-text").innerHTML = " person said yes!"
      } else {
        document.getElementById("vote-text").innerText = " people have said yes!"
      }
    }
  })
}