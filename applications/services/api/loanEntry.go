package main

import (
	"net/http"

	eh "github.com/andreasvikke-school/CPH-Bussiness-SI-Exam/applications/services/api/errorhandler"
	"github.com/gin-gonic/gin"
)

type LoanEntry struct {
	UserId   int64 `json:"userId,omitempty"`
	EntityId int64 `json:"entityId,omitempty"`
}

func CreateLoanEntry(c *gin.Context) {
	var loanEntry LoanEntry
	err := c.BindJSON(&loanEntry)
	eh.PanicOnError(err, "Couldn't bind JSON")
	ProduceLoanEntryToRabbitmq(loanEntry)
	c.IndentedJSON(http.StatusOK, gin.H{
		"queued": "success",
	})
}