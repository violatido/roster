function addVote(id){
  $.ajax ({
    url: '/roster/update-vote-count',
    type: "GET",
    data: {
      employee_id : id,
    },
    success: function(data) {
      document.getElementById(`vote-count-${id}`).innerHTML = `${data["vote_count"]}`;
    }
  })
}