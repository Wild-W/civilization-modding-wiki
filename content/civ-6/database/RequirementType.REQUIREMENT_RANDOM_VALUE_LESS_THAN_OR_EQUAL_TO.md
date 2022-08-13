---
tags:
- RequirementType
title: REQUIREMENT_RANDOM_VALUE_LESS_THAN_OR_EQUAL_TO
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_RANDOM_VALUE_LESS_THAN_OR_EQUAL_TO
>
> * Class: `Unknown`
> * Arguments:
>	* Scaling `Unknown`
>	* PopulationScaling `Unknown`
>	* Index `Unknown`
>	* Chance `Unknown`

## Samples

```SQL {title="REQUIREMENT_ZOMBIE_PERCENT_CHANCE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIREMENT_ZOMBIE_PERCENT_CHANCE",
		"REQUIREMENT_RANDOM_VALUE_LESS_THAN_OR_EQUAL_TO"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIREMENT_ZOMBIE_PERCENT_CHANCE",
		"Chance",
		20
	),
	(
		"REQUIREMENT_ZOMBIE_PERCENT_CHANCE",
		"Index",
		0
	),
	(
		"REQUIREMENT_ZOMBIE_PERCENT_CHANCE",
		"Scaling",
		"SCALING_HALF"
	);
	
```

```SQL {title="REQUIREMENT_DISTRICT_ZOMBIE_EFFECT_PERCENT_CHANCE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIREMENT_DISTRICT_ZOMBIE_EFFECT_PERCENT_CHANCE",
		"REQUIREMENT_RANDOM_VALUE_LESS_THAN_OR_EQUAL_TO"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIREMENT_DISTRICT_ZOMBIE_EFFECT_PERCENT_CHANCE",
		"Chance",
		2
	),
	(
		"REQUIREMENT_DISTRICT_ZOMBIE_EFFECT_PERCENT_CHANCE",
		"Index",
		0
	),
	(
		"REQUIREMENT_DISTRICT_ZOMBIE_EFFECT_PERCENT_CHANCE",
		"PopulationScaling",
		1
	);
	
```
