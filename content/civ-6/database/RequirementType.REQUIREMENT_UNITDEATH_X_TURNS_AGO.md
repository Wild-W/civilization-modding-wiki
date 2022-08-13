---
tags:
- RequirementType
title: REQUIREMENT_UNITDEATH_X_TURNS_AGO
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNITDEATH_X_TURNS_AGO
>
> * Class: `Unknown`
> * Arguments:
>	* Turns `Unknown`
>	* ScalingType `Unknown`
>	* Scaling `Unknown`

## Samples

```SQL {title="HAS_BEEN_ZOMBIE_RESPAWN_TURNS_LONGER_AGAIN_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"HAS_BEEN_ZOMBIE_RESPAWN_TURNS_LONGER_AGAIN_REQUIREMENT",
		"REQUIREMENT_UNITDEATH_X_TURNS_AGO"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"HAS_BEEN_ZOMBIE_RESPAWN_TURNS_LONGER_AGAIN_REQUIREMENT",
		"Scaling",
		1
	),
	(
		"HAS_BEEN_ZOMBIE_RESPAWN_TURNS_LONGER_AGAIN_REQUIREMENT",
		"ScalingType",
		"SCALING_HALF"
	),
	(
		"HAS_BEEN_ZOMBIE_RESPAWN_TURNS_LONGER_AGAIN_REQUIREMENT",
		"Turns",
		150
	);
	```

```SQL {title="HAS_BEEN_ONE_TURN_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"HAS_BEEN_ONE_TURN_REQUIREMENT",
		"REQUIREMENT_UNITDEATH_X_TURNS_AGO"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"HAS_BEEN_ONE_TURN_REQUIREMENT",
		"Turns",
		1
	);
	```
