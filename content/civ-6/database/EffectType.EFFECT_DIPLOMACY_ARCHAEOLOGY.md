---
tags:
- EffectType
title: EFFECT_DIPLOMACY_ARCHAEOLOGY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_ARCHAEOLOGY
>
> * Class: `PLAYERS`
> * Parameters:
>	* DiplomacyKey `String`
>	* IncrementValue `Integer`
>	* InitialValue `Integer`
>	* MessageThrottle `Integer`
>	* ModifierPerTransgression `Integer`
>	* SimpleModifierDescription `String`

## Samples

```SQL {title="STANDARD_DIPLOMATIC_ARCHAEOLOGY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_ARCHAEOLOGY",
		"MODIFIER_PLAYER_DIPLOMACY_ARCHAEOLOGY",
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
		"STANDARD_DIPLOMATIC_ARCHAEOLOGY",
		"DiplomacyKey",
		"WARNING_STOP_DIGGING_UP_ARTIFACTS"
	),
	(
		"STANDARD_DIPLOMATIC_ARCHAEOLOGY",
		"IncrementValue",
		0
	),
	(
		"STANDARD_DIPLOMATIC_ARCHAEOLOGY",
		"InitialValue",
		0
	),
	(
		"STANDARD_DIPLOMATIC_ARCHAEOLOGY",
		"MessageThrottle",
		20
	),
	(
		"STANDARD_DIPLOMATIC_ARCHAEOLOGY",
		"ModifierPerTransgression",
		"-5"
	),
	(
		"STANDARD_DIPLOMATIC_ARCHAEOLOGY",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_STOP_DIGGING_UP_ARTIFACTS_WARNING"
	);
	
```

