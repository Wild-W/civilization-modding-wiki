---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_EXPLORATION_LEAD
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_EXPLORATION_LEAD
>
> * Class: `PLAYERS`
> * Arguments:
>	* MinimumDelta `Integer`
>	* ExplorationRatio `Integer`

## Samples

```SQL {title="REQUIRES_HAS_HIGH_EXPLORATION"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_EXPLORATION",
		"REQUIREMENT_PLAYER_EXPLORATION_LEAD"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_EXPLORATION",
		"ExplorationRatio",
		"1.1"
	),
	(
		"REQUIRES_HAS_HIGH_EXPLORATION",
		"MinimumDelta",
		5
	);
	
```
