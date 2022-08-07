---
tags:
- EffectType
title: EFFECT_DIPLOMACY_SETTLED_CITIES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_SETTLED_CITIES
>
> * Class: `PLAYERS`
> * Parameters:
>	* DiplomacyKey `String`
>	* IncrementValue `Integer`
>	* InitialValue `Integer`
>	* MessageThrottle `Integer`
>	* ReductionTurns `Integer`
>	* ReductionValue `Integer`
>	* SimpleModifierDescription `String`

## Samples

```SQL {title="STANDARD_DIPLOMACY_SETTLED_CITIES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMACY_SETTLED_CITIES",
		"MODIFIER_PLAYER_DIPLOMACY_SETTLED_CITIES",
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
		"STANDARD_DIPLOMACY_SETTLED_CITIES",
		"DiplomacyKey",
		"WARNING_DONT_SETTLE_NEAR_ME"
	),
	(
		"STANDARD_DIPLOMACY_SETTLED_CITIES",
		"IncrementValue",
		0
	),
	(
		"STANDARD_DIPLOMACY_SETTLED_CITIES",
		"InitialValue",
		0
	),
	(
		"STANDARD_DIPLOMACY_SETTLED_CITIES",
		"MessageThrottle",
		20
	),
	(
		"STANDARD_DIPLOMACY_SETTLED_CITIES",
		"ReductionTurns",
		10
	),
	(
		"STANDARD_DIPLOMACY_SETTLED_CITIES",
		"ReductionValue",
		"-1"
	),
	(
		"STANDARD_DIPLOMACY_SETTLED_CITIES",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_SETTLED_NEAR_BORDER_WARNING"
	);
	
```

