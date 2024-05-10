# TableTopTales API

The testing documentation provides an overview of all testing conducted on TableTopTales API. Covering Validation, automated tests and manual testing. 

### Validation

All the code has been run through Code Institute [CI Python Linter](https://pep8ci.herokuapp.com/). All code passed, except for some minor issues with whitespace and long lines. 

### Manual testing

Testing of the backend API has been done throughout the development process, both by posting and fetching data through the front end as well as through the Django Rest interface. 

#### Reviews
| Feature | Action | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| list | view reviews | view reviews in list | pass |
| form | logged in | view create review form | pass |
| form | logged out | cannot view create review form | pass |
| post button | click | submit form and create review | pass |
| filter button | click | filter and order reviews | pass |

#### Reviews-id
| Feature | Action | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| review | view review | view a single review | pass |
| form | logged in | for own review but not others: view edit review form and delete button | pass |
| form | logged out | cannot view edit review form and delete button | pass |
| get button | click | submit form and edit review | pass |
| delete button | click | delete review | pass |

#### Games(wishlist)
| Feature | Action | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| list | view games | view games in list | pass |
| form | logged in | access create games form | pass |
| form | logged out | cannot access create games form | pass |
| post button | click | submit form and games story | pass |
| filter button | click | filter and order games | pass |

#### Game-id endpoint
| Feature | Action | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| game | view game | view game | pass |
| form | logged in | for own game but not others: access edit game form and delete button | pass |
| form | logged out | cannot access edit game form and delete button | pass |
| get button | click | submit form and edit game | pass |
| delete button | click | delete game | pass |

#### Likes
| Feature | Action | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| list | view likes | view likes in list | pass |
| form | logged in | view create like form | pass |
| form | logged out | cannot view create like form | pass |
| post button | click | submit form and create like | pass |

#### Likes-id
| Feature | Action | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| like | view like | view like | pass |
| delete button | logged in | for own like but not others: view delete button | pass |
| delete button | logged out | cannot view delete button | pass |
| delete button | click | delete like | pass |

#### Saved
| Feature | Action | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| list | view saved | view saved in list | pass |
| form | logged in | view create saved form | pass |
| form | logged out | cannot view create saved form | pass |
| post button | click | submit form and create saved | pass |

#### Saved-id
| Feature | Action | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| save | view saved | view saved | pass |
| delete button | logged in | for own saved but not others: view delete button | pass |
| delete button | logged out | cannot view delete button | pass |
| delete button | click | remove a save | pass |

#### Comments
| Feature | Action | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| list | view comments | view comments in list | pass |
| form | logged in | access create comment form | pass |
| form | logged out | cannot access create comment form | pass |
| post button | click | submit form and create comment | pass |
| filter button | click | filter and order comments | pass |

#### Comments-id
| Feature | Action | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| comment | view comment | view comment | pass |
| form | logged in | for own comment but not others: access edit comment form and delete button | pass |
| form | logged out | cannot access edit comment form and delete button | pass |
| get button | click | submit form and edit comment | pass |
| delete button | click | delete comment | pass |

#### Profiles
| Feature | Action | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| list | view profiles | view profiles in list | pass |

#### Profiles-id
| Feature | Action | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| profile | view profile | view profile | pass |
| form | logged in | for own profile but not others: access edit profile form and delete button | pass |
| form | logged out | cannot access edit profile form and delete button | pass |
| get button | click | submit form and edit profile | pass |
| delete button | click | delete profile | pass |


