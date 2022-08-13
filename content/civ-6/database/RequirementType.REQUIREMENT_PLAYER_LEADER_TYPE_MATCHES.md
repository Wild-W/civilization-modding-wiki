---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_LEADER_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_LEADER_TYPE_MATCHES
>
> * Class: `PLAYERS`
> * Arguments:
>	* LeaderType `String`
>		* [Leaders.LeaderType]

## Samples

```SQL {title="REQUIREMENT_NUBIA_SCENARIO_PLAYER_IS_NUBIA"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIREMENT_NUBIA_SCENARIO_PLAYER_IS_NUBIA",
		"REQUIREMENT_PLAYER_LEADER_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIREMENT_NUBIA_SCENARIO_PLAYER_IS_NUBIA",
		"LeaderType",
		"LEADER_AMANITORE"
	);
	```
