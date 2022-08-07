---
tags:
- EffectType
title: EFFECT_DIPLOMACY_THIRD_PARTY_EFFECTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_THIRD_PARTY_EFFECTS
>
> * Class: `PLAYERS`
> * Parameters:
>	* AmountPerIncident `Integer`
>	* EffectType `String`
>	* IncrementValue `Integer`
>	* InitialValue `Integer`
>	* MaxEffectMagnitude `Integer`
>	* SimpleModifierDescription `String`

## Samples
```SQL {title="STANDARD_DIPLOMATIC_3RD_PARTY_DECLARED_SURPRISE_WAR_ON_FRIEND"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_3RD_PARTY_DECLARED_SURPRISE_WAR_ON_FRIEND",
		"MODIFIER_PLAYER_DIPLOMACY_THIRD_PARTY_EFFECTS",
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
		"STANDARD_DIPLOMATIC_3RD_PARTY_DECLARED_SURPRISE_WAR_ON_FRIEND",
		"AmountPerIncident",
		"-8"
	),
	(
		"STANDARD_DIPLOMATIC_3RD_PARTY_DECLARED_SURPRISE_WAR_ON_FRIEND",
		"EffectType",
		"DeclaredSurpriseWarOnFriend"
	),
	(
		"STANDARD_DIPLOMATIC_3RD_PARTY_DECLARED_SURPRISE_WAR_ON_FRIEND",
		"IncrementValue",
		0
	),
	(
		"STANDARD_DIPLOMATIC_3RD_PARTY_DECLARED_SURPRISE_WAR_ON_FRIEND",
		"InitialValue",
		0
	),
	(
		"STANDARD_DIPLOMATIC_3RD_PARTY_DECLARED_SURPRISE_WAR_ON_FRIEND",
		"MaxEffectMagnitude",
		8
	),
	(
		"STANDARD_DIPLOMATIC_3RD_PARTY_DECLARED_SURPRISE_WAR_ON_FRIEND",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_DECLARED_SURPRISE_WAR_ON_FRIEND"
	);
	
```

