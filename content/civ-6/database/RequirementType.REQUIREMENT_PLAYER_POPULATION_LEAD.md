---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_POPULATION_LEAD
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_POPULATION_LEAD
>
> * Class: `PLAYERS`
> * Arguments:
>	* PopulationRatio `Integer`
>	* MinimumDelta `Integer`

## Samples

```SQL {title="REQUIRES_HAS_HIGH_POPULATION"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_POPULATION",
		"REQUIREMENT_PLAYER_POPULATION_LEAD"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_POPULATION",
		"MinimumDelta",
		3
	),
	(
		"REQUIRES_HAS_HIGH_POPULATION",
		"PopulationRatio",
		"1.1"
	);
	
```
