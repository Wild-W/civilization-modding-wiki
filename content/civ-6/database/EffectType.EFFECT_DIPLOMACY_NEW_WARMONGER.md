---
tags:
- EffectType
title: EFFECT_DIPLOMACY_NEW_WARMONGER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_NEW_WARMONGER
>
> * Class: `PLAYERS`
> * Parameters:
>	* LowerLimit `Integer`
>	* PercentOfGrievances `Integer`
>	* ReductionTurns `Integer`
>	* ReductionValue `Integer`

## Samples

```SQL {title="STANDARD_DIPLOMATIC_WARMONGER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_WARMONGER",
		"MODIFIER_PLAYER_DIPLOMACY_NEW_WARMONGER",
		"ON_TURN_STARTED",
		"PLAYER_IS_NEW_WARMONGER_SUBJECT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_WARMONGER",
		"LowerLimit",
		"-60"
	),
	(
		"STANDARD_DIPLOMATIC_WARMONGER",
		"PercentOfGrievances",
		20
	),
	(
		"STANDARD_DIPLOMATIC_WARMONGER",
		"ReductionTurns",
		2
	),
	(
		"STANDARD_DIPLOMATIC_WARMONGER",
		"ReductionValue",
		"-1"
	);
	
```

