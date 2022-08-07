---
tags:
- EffectType
title: EFFECT_DIPLOMACY_KEPT_PLEDGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_KEPT_PLEDGE
>
> * Class: `PLAYERS`
> * Parameters:
>	* IncrementValue `Integer`
>	* InitialValue `Integer`
>	* ModifierPerKeptPledge `Integer`
>	* ReductionTurns `Integer`
>	* ReductionValue `Integer`
>	* SimpleModifierDescription `String`

## Samples
```SQL {title="STANDARD_DIPLOMATIC_KEPT_PLEDGE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_KEPT_PLEDGE",
		"MODIFIER_PLAYER_DIPLOMACY_KEPT_PLEDGE",
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
		"STANDARD_DIPLOMATIC_KEPT_PLEDGE",
		"IncrementValue",
		0
	),
	(
		"STANDARD_DIPLOMATIC_KEPT_PLEDGE",
		"InitialValue",
		0
	),
	(
		"STANDARD_DIPLOMATIC_KEPT_PLEDGE",
		"ModifierPerKeptPledge",
		4
	),
	(
		"STANDARD_DIPLOMATIC_KEPT_PLEDGE",
		"ReductionTurns",
		15
	),
	(
		"STANDARD_DIPLOMATIC_KEPT_PLEDGE",
		"ReductionValue",
		1
	),
	(
		"STANDARD_DIPLOMATIC_KEPT_PLEDGE",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_KEPT_PLEDGE"
	);
	
```

