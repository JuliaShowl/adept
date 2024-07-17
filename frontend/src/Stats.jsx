import React from 'react'

const Statistics = ({stats}) => {
    return <div>
        Total Documents ({stats.totalDocuments}) 
        In Draft ({stats.inDraft})
        In Review ({stats.inReview})
        Pending Approval ({stats.pendingApproval})
        Complete ({stats.complete})

    </div>
}

export default Statistics