---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_SUZERAIN_OF_X
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_SUZERAIN_OF_X
>
> * Class: `PLAYERS`
> * Arguments:
>	* LeaderType `String`
>		* [Leaders.LeaderType]

## Samples

```SQL {title="PLAYER_HAS_LAHORE_SUZERAIN"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"PLAYER_HAS_LAHORE_SUZERAIN",
		"REQUIREMENT_PLAYER_IS_SUZERAIN_OF_X"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"PLAYER_HAS_LAHORE_SUZERAIN",
		"LeaderType",
		"LEADER_MINOR_CIV_LAHORE"
	);
	
```
