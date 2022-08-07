---
tags:
- EffectType
title: EFFECT_DIPLOMACY_ESPIONAGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_ESPIONAGE
>
> * Class: `PLAYERS`
> * Parameters:
>	* DiplomacyKey `String`
>	* IncrementValue `Integer`
>	* InitialValue `Integer`
>	* MessageThrottle `Integer`
>	* ModifierPerTransgression `Integer`
>	* ReductionTurns `Integer`
>	* ReductionValue `Integer`
>	* SimpleModifierDescription `String`

## Samples
```SQL {title="STANDARD_DIPLOMATIC_ESPIONAGE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_ESPIONAGE",
		"MODIFIER_PLAYER_DIPLOMACY_ESPIONAGE",
		"ON_ESPIONAGE_DETECTED"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_ESPIONAGE",
		"DiplomacyKey",
		"WARNING_STOP_SPYING_ON_ME"
	),
	(
		"STANDARD_DIPLOMATIC_ESPIONAGE",
		"IncrementValue",
		0
	),
	(
		"STANDARD_DIPLOMATIC_ESPIONAGE",
		"InitialValue",
		0
	),
	(
		"STANDARD_DIPLOMATIC_ESPIONAGE",
		"MessageThrottle",
		20
	),
	(
		"STANDARD_DIPLOMATIC_ESPIONAGE",
		"ModifierPerTransgression",
		"-5"
	),
	(
		"STANDARD_DIPLOMATIC_ESPIONAGE",
		"ReductionTurns",
		15
	),
	(
		"STANDARD_DIPLOMATIC_ESPIONAGE",
		"ReductionValue",
		1
	),
	(
		"STANDARD_DIPLOMATIC_ESPIONAGE",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_STOP_SPYING_ON_ME_WARNING"
	);
	
```

