---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_SUZERAIN_X_TYPE
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_SUZERAIN_X_TYPE
>
> * Class: `PLAYERS`
> * Arguments:
>	* LeaderType `String`
>		* [Leaders.LeaderType]
>	* Amount `Integer`

## Samples

```SQL {title="REQUIRES_SUZERAIN_CULTURAL_1_LEADER"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_SUZERAIN_CULTURAL_1_LEADER",
		"REQUIREMENT_PLAYER_IS_SUZERAIN_X_TYPE"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_SUZERAIN_CULTURAL_1_LEADER",
		"Amount",
		1
	),
	(
		"REQUIRES_SUZERAIN_CULTURAL_1_LEADER",
		"LeaderType",
		"LEADER_MINOR_CIV_CULTURAL"
	);
	```
