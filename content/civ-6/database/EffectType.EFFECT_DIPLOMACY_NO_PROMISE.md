---
tags:
- EffectType
title: EFFECT_DIPLOMACY_NO_PROMISE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_NO_PROMISE
>
> * Class: `PLAYERS`
> * Parameters:
>	* IncrementValue `Integer`
>	* ModifierPerTransgression `Integer`
>	* ReductionTurns `Integer`
>	* ReductionValue `Integer`
>	* SimpleModifierDescription `String`

## Samples
```SQL {title="STANDARD_DIPLOMATIC_NO_PROMISE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_NO_PROMISE",
		"MODIFIER_PLAYER_DIPLOMACY_NO_PROMISE",
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
		"STANDARD_DIPLOMATIC_NO_PROMISE",
		"IncrementValue",
		0
	),
	(
		"STANDARD_DIPLOMATIC_NO_PROMISE",
		"ModifierPerTransgression",
		"-3"
	),
	(
		"STANDARD_DIPLOMATIC_NO_PROMISE",
		"ReductionTurns",
		10
	),
	(
		"STANDARD_DIPLOMATIC_NO_PROMISE",
		"ReductionValue",
		1
	),
	(
		"STANDARD_DIPLOMATIC_NO_PROMISE",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_NO_PROMISE"
	);
	
```

