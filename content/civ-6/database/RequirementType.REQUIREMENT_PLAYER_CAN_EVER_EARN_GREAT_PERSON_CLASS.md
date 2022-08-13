---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_CAN_EVER_EARN_GREAT_PERSON_CLASS
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_CAN_EVER_EARN_GREAT_PERSON_CLASS
>
> * Class: `PLAYERS`
> * Arguments:
>	* GreatPersonClass `String`

## Samples

```SQL {title="REQUIRES_PLAYER_CAN_EVER_EARN_PROPHET"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_CAN_EVER_EARN_PROPHET",
		"REQUIREMENT_PLAYER_CAN_EVER_EARN_GREAT_PERSON_CLASS"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLAYER_CAN_EVER_EARN_PROPHET",
		"GreatPersonClass",
		"GREAT_PERSON_CLASS_PROPHET"
	);
	```
