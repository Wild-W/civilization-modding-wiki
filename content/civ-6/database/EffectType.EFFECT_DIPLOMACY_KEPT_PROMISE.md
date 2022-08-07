---
tags:
- EffectType
title: EFFECT_DIPLOMACY_KEPT_PROMISE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_KEPT_PROMISE
>
> * Class: `PLAYERS`
> * Parameters:
>	* IncrementValue `Integer`
>	* InitialValue `Integer`
>	* ModifierPerKeptPromise `Integer`
>	* ReductionTurns `Integer`
>	* ReductionValue `Integer`
>	* SimpleModifierDescription `String`

## Samples
```SQL {title="STANDARD_DIPLOMATIC_KEPT_PROMISE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_KEPT_PROMISE",
		"MODIFIER_PLAYER_DIPLOMACY_KEPT_PROMISE",
		"ON_TURN_STARTED",
		"PLAYER_IS_KNOWN_MAJOR_CIV"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_KEPT_PROMISE",
		"IncrementValue",
		0
	),
	(
		"STANDARD_DIPLOMATIC_KEPT_PROMISE",
		"InitialValue",
		0
	),
	(
		"STANDARD_DIPLOMATIC_KEPT_PROMISE",
		"ModifierPerKeptPromise",
		4
	),
	(
		"STANDARD_DIPLOMATIC_KEPT_PROMISE",
		"ReductionTurns",
		15
	),
	(
		"STANDARD_DIPLOMATIC_KEPT_PROMISE",
		"ReductionValue",
		1
	),
	(
		"STANDARD_DIPLOMATIC_KEPT_PROMISE",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_KEPT_PROMISE"
	);
	
```

