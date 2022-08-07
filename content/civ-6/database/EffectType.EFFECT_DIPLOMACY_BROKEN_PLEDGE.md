---
tags:
- EffectType
title: EFFECT_DIPLOMACY_BROKEN_PLEDGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_BROKEN_PLEDGE
>
> * Class: `PLAYERS`
> * Parameters:
>	* IncrementValue `Integer`
>	* ModifierPerTransgression `Integer`
>	* ReductionTurns `Integer`
>	* ReductionValue `Integer`
>	* SimpleModifierDescription `String`

## Samples

```SQL {title="STANDARD_DIPLOMATIC_BROKEN_PLEDGE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_BROKEN_PLEDGE",
		"MODIFIER_PLAYER_DIPLOMACY_BROKEN_PLEDGE",
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
		"STANDARD_DIPLOMATIC_BROKEN_PLEDGE",
		"IncrementValue",
		0
	),
	(
		"STANDARD_DIPLOMATIC_BROKEN_PLEDGE",
		"ModifierPerTransgression",
		"-6"
	),
	(
		"STANDARD_DIPLOMATIC_BROKEN_PLEDGE",
		"ReductionTurns",
		15
	),
	(
		"STANDARD_DIPLOMATIC_BROKEN_PLEDGE",
		"ReductionValue",
		1
	),
	(
		"STANDARD_DIPLOMATIC_BROKEN_PLEDGE",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_BROKEN_PLEDGE"
	);
	
```

