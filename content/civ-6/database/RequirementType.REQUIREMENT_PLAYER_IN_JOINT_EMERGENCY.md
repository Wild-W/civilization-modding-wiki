---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IN_JOINT_EMERGENCY
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IN_JOINT_EMERGENCY
>
> * Class: `PLAYERS`
> * Arguments:
>	* HostileOnly `Boolean`

## Samples

```SQL {title="REQUIRES_SHARED_EMERGENCY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_SHARED_EMERGENCY",
		"REQUIREMENT_PLAYER_IN_JOINT_EMERGENCY"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_SHARED_EMERGENCY",
		"HostileOnly",
		1
	);
	
```
